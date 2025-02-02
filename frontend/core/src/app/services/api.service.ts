import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private APIURL = 'http://localhost:8000/v1/api';

  constructor(private http: HttpClient) { }

  testData() {
    return this.http.get(`${this.APIURL}/data`);
  }
}
