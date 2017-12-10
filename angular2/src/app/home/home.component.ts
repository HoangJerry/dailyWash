import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { AppService }        from '../app.service';
import { Router } 				from '@angular/router';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.css'],
	encapsulation: ViewEncapsulation.None,
})
export class HomeComponent implements OnInit {
	products = [];
	categories;
	errors;
	constructor(
				private _api: AppService,
				private _router: Router,
		) { 
			this._api.CategoriesList()
			.subscribe(
					(res:any) => {
						this.categories = res.results;
						// console.log(this.categories);
						this.categories.forEach((c)=>{
							this._api.ProductByCategory(c.id)
							.subscribe(
								(res:any) => {
									c.products = res.results;
									// res.results.forEach((d)=>{
									// 	this.products.push(d);
									// });
								},
								(error:any) =>  this.errors = error
							);
						})
					},
					(error:any) =>  {this.errors = error},
				);
			this._api.ProductList()
			.subscribe(
				(res:any) => {
					this.products = res.results;
				},
				(error:any) =>  {this.errors = error},
			);
		}

	ngOnInit() {
	}
	onClickOrder(product_id){
		product_id = JSON.stringify(product_id);
		localStorage.setItem('product',product_id);
		// console.log(product_id);
		this._router.navigate(['order']);
	}
		

}
