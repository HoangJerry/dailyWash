import { Component, OnInit } 	from '@angular/core';
import { Router }				from '@angular/router';

import { IUser }				from '../app'

import { AppService }   		from '../app.service';


@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {
	users = [];
    errors = [];
    selectedId = 0;
    constructor(private _router: Router, private _api: AppService){

    };
  	ngOnInit() {
	    this._api.UserList()
	        .subscribe(
	            (res:any) => {
	            	console.log(res);
	             	this.users = res.results;
	            },
	            (error:any) =>  this.errors = <any>error
	        );
	};

	delUser(event:any,id) {
		event.preventDefault();
		console.log(id);
		this._api.UserDelete(id)
			.subscribe(
	            (res:any) => {
	            	console.log(res);
	            	this.ngOnInit()
	            },
	            (error:any) =>  this.errors = <any>error
	        );
	}
	
}
