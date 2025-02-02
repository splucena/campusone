import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './services/api.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [ApiService]
})
export class AppComponent implements OnInit{
  title = 'CampusOne Frontend';
  testData: any;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
      this.apiService.testData().subscribe(data => {
        this.testData = data;
      })
  }
}
