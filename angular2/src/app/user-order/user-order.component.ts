import { Component, OnInit } from '@angular/core';
import { AppService }        from '../app.service';

@Component({
  selector: 'app-user-order',
  templateUrl: './user-order.component.html',
  styleUrls: ['./user-order.component.css']
})
export class UserOrderComponent implements OnInit {

  CityData:any;
  District:any;
  
  constructor(
    private _api:AppService
  ) { }

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
