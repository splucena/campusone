# Use the official Golang image
FROM golang:1.22 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Go module files
COPY go.mod go.sum ./
RUN go mod download

# Copy the source code
COPY . .

# Build the application
RUN go build -o proctorgo

# Create a lightweight runtime image
FROM debian:bookworm-slim

# Set the working directory
WORKDIR /root/

# Copy the built binary from the builder stage
COPY --from=builder /app/proctorgo .

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["./proctorgo"]
