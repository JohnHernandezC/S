import { Injectable } from '@angular/core';
import{HttpClient} from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class PostService {
  api_link: string="http://localhost:8000"

  constructor(private http: HttpClient) { }
  getAllPost(){
    return this.http.get(this.api_link+`/cuentas/`)//aqui
  }
}
