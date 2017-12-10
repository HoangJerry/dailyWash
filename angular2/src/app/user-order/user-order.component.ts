import { Component, OnInit } from '@angular/core';
import { AppService }        from '../app.service';
import { Router }	           from '@angular/router';
import { OrderType }         from '../data-type/order';
@Component({
  selector: 'app-user-order',
  templateUrl: './user-order.component.html',
  styleUrls: ['./user-order.component.css']
})
export class UserOrderComponent implements OnInit {
  user = {
      first_name:"",
      last_name:"",
      address:"",
  };
  product;
  order =  new OrderType;
  foods = [
    {value: '0', viewValue: 'Choose taking-time'},
    {value: '1', viewValue: '5 - 7'},
    {value: '2', viewValue: '11 - 13'},
    {value: '3', viewValue: '18 - 20'}
  ];
    constructor(private _router: Router, private _api: AppService) {
      try {
          this.product = localStorage.getItem('product');
          this.product = JSON.parse(this.product);
          // localStorage.removeItem('product');
      }
      catch(err) {
          
      }
      // this.product
  	  this._api.UserMe()
  		.subscribe(
  			(res:any)=>{
  				this.user=res.results[0];
          this.order.estimate =0;
          this.order.time_taking =0;
  				this.order.taking_address= res.results[0].address;
          this.order.returning_address=res.results[0].address;
  			})
  }

  ngOnInit() {
  }
  onClickOrder(){
    console.log(this.order);
  }
}
