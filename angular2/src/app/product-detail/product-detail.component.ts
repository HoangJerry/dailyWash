import { Component, OnInit } from '@angular/core';
import { Router,ActivatedRoute, Params } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {
  product:any;
  errors;



  constructor(
  	private _router: Router, 
  	private _api: AppService, 
  	private route:ActivatedRoute,
  	) { 
      route.params.subscribe((value)=> {
        this.ProductDetail(value.id)
      });
  }

  ngOnInit() {
  }
  ProductDetail(id){
    this._api.ProductList("",id)
        //Product detail
        .subscribe(
          (res:any) => {
            this.product = res.results[0];
            // console.log(this.product);
          },
          (error:any) =>  {this.errors = error},
        );

  }
}
