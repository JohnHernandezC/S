import { Component, OnInit } from '@angular/core';
import{PostService} from '../post.service';

@Component({
  selector: 'app-post-component',
  templateUrl: './post-component.component.html',
  styleUrls: ['./post-component.component.css']
})
export class PostComponentComponent implements OnInit {
  posts:any;
  constructor(private pService: PostService) { }
  ngOnInit():void {
    this.AllPost();
  }

  AllPost(){
    this.pService.getAllPost().subscribe(posts =>{
      this.posts=posts;
      console.log(this.posts)
    })
  }
  

}
