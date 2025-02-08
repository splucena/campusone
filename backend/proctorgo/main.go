package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gorilla/websocket"
	"github.com/pion/webrtc/v3"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

var mongoClient *mongo.Client

func main() {
	// Load environment variables
	port := os.Getenv("APP_PORT")
	if port == "" {
		port = "8080"
	}
	mongoURI := os.Getenv("MONGO_URI")
	if mongoURI == "" {
		mongoURI = "mongodb://localhost:27017"
	}

	// Connect to MongoDB
	var err error
	mongoClient, err = mongo.Connect(context.TODO(), options.Client().ApplyURI(mongoURI))
	if err != nil {
		log.Fatalf("Failed to connect to MongoDB: %v", err)
	}
	defer mongoClient.Disconnect(context.TODO())

	log.Println("Connected to MongoDB")

	// Define routes
	http.HandleFunc("/ws", handleWebSocket)
	http.HandleFunc("/webrtc", handleWebRTC)

	log.Println("ProctorGo running on port", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

// WebSocket handler for real-time proctoring alerts
func handleWebSocket(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println("WebSocket upgrade failed:", err)
		return
	}
	defer conn.Close()

	log.Println("WebSocket client connected")

	for {
		_, msg, err := conn.ReadMessage()
		if err != nil {
			log.Println("WebSocket error:", err)
			break
		}
		log.Printf("Received message: %s\n", msg)

		// Example: Store event in MongoDB
		storeProctoringEvent(string(msg))

		// Echo message back to client
		conn.WriteMessage(websocket.TextMessage, []byte("Received: "+string(msg)))
	}
}

// WebRTC handler (placeholder for video/audio streaming)
func handleWebRTC(w http.ResponseWriter, r *http.Request) {
	peerConnection, err := webrtc.NewPeerConnection(webrtc.Configuration{})
	if err != nil {
		http.Error(w, "Failed to create WebRTC connection", http.StatusInternalServerError)
		log.Println("WebRTC error:", err)
		return
	}
	defer peerConnection.Close()

	fmt.Fprintln(w, "WebRTC connection established")
}

// Store a proctoring event in MongoDB
func storeProctoringEvent(event string) {
	collection := mongoClient.Database("proctor").Collection("events")
	_, err := collection.InsertOne(context.TODO(), map[string]string{"event": event})
	if err != nil {
		log.Println("Failed to insert event into MongoDB:", err)
	}
}
