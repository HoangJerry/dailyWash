import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { AppService }         from '../app.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class SignupComponent implements OnInit {
	cities;
	districts;
	citySelected;
	districtSelected;
	firstNameType;
	lastNameType;
	emailType;
	phoneType;
	addressType;

	errors;
  constructor(
  	private _api: AppService,
  ) {
  	this._api.CitiesList()
	  		.subscribe(
	          (res:any) => {
	            this.cities = res.results;
	          },
	          (error:any) =>  this.errors = error
	      );
  }

  ngOnInit() {
  }

  onChangeCity(obj){
  	this.citySelected=obj;
  	this._api.DistrictsList(this.citySelected.id)
  			.subscribe(
	          (res:any) => {
	            this.districts = res.results;
	          },
	          (error:any) =>  this.errors = error
	      );
  }

}
