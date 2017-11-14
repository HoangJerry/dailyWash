import { Component, OnInit } from '@angular/core';
import { AppService }        from '../app.service';
import { DateAdapter, NativeDateAdapter } from '@angular/material';
import { ViewChild } from '@angular/core'
@Component({
  selector: 'app-user-order',
  templateUrl: './user-order.component.html',
  styleUrls: ['./user-order.component.css']
})
export class UserOrderComponent implements OnInit {
  user;
  minDate = new Date(2000, 0, 1);
  maxDate = new Date(2020, 0, 1);
  CityData:any;
  District:any;
  
  constructor(
    private _api:AppService,
  ) {
    this.user=JSON.parse(localStorage.getItem('body'));
    this.userDetail();
  }

  public userDetail(){
    this._api.UserDetail(this.user.id)
      .subscribe(
        (res:any)=>{
          this.user=res
          if (this.user.phone[0]==0)
            {this.user.phone=this.user.phone.substr(1)} 
          console.log()
        },
      )
  }

  ngOnInit() {
    this._api.CityData()
        .subscribe(res=>{
      this.CityData = res.results;
    })
    
  }


  public chooseCity(id){
    this._api.DistrictData(id)
        .subscribe(res=>{
      this.District = res.results;
    })
  }



}
