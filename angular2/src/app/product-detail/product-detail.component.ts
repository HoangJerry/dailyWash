import { Component, OnInit } from '@angular/core';
import { Router,ActivatedRoute, Params } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {

  constructor(
  	private _router: Router, 
  	private _api: AppService, 
  	private route:ActivatedRoute,
  	) { console.log(route.params);}

  ngOnInit() {
  }

}
