import { Component, OnInit, Input	 } from '@angular/core';
import { Router,ActivatedRoute, Params } from '@angular/router';

import { AppService } from '../app.service';
@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.css']
})
export class UserDetailComponent implements OnInit {
	user = '';
	errors = [];
    constructor(private _router: Router, private _api: AppService, private route:ActivatedRoute){
    	console.log(route.params);
    	route.params.subscribe((value)=> {
  			this.GetUserDetail(value.id)
		});
    };
	ngOnInit() {
	}

	GetUserDetail(id) {
		this._api.UserDetail(id)
	        .subscribe(
	            (res:any) => {
	            	console.log(res);
	             	this.user = res;
	            },
	            (error:any) =>  this.errors = <any>error
	        );
	} 

}
