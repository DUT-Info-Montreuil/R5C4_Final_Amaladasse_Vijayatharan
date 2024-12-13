import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-liste',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './liste.component.html',
  styleUrls: ['./liste.component.css']
})
export class ListeComponent implements OnInit {
  data: any[] = []; 
  paginatedData: any[] = [];
  currentPage: number = 1;
  itemsPerPage: number = 30;

  constructor(private readonly http: HttpClient) {}

  ngOnInit(): void {

    this.http.get<any[]>('http://127.0.0.1:5000/searches/all').subscribe((response) => {
      this.data = response;
      console.log(this.data);
      this.updatePagination(); 
    });
  }

  updatePagination(): void {
    const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    const endIndex = this.currentPage * this.itemsPerPage;
    this.paginatedData = this.data.slice(startIndex, endIndex);
  }

  nextPage(): void {
    if (this.currentPage * this.itemsPerPage < this.data.length) {
      this.currentPage++;
      this.updatePagination();
    }
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.updatePagination();
    }
  }
}
