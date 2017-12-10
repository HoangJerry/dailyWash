import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { AppService }         from '../app.service';
import { Router } from '@angular/router'
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
		private _router: Router,
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
  onClickRegister(){
  	if (this.citySelected && this.districtSelected && this.firstNameType &&
		this.lastNameType && this.emailType && this.phoneType && 
		this.addressType){
	  		this._api.UserSignUp(this.firstNameType,this.lastNameType,this.citySelected.id,
	  			this.districtSelected.id,this.addressType,this.emailType,this.phoneType)
	  			.subscribe(
		          (res:any) => {
		            this._router.navigate(['/success']);
		          },
	          // (error:any) =>  this.errors = error
			);
  		}
  	else{
  		this.errors = "Please fill all the field"
  	}
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
