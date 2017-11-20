import { Component, OnInit } from '@angular/core';
import { Router }	         from '@angular/router';

@Component({
	selector: 'app-dashboard-main',
	templateUrl: './dashboard-main.component.html',
	styleUrls: ['./dashboard-main.component.css']
})
export class DashboardMainComponent implements OnInit {
	user;
	constructor(private _router: Router) {
		this.user=JSON.parse(localStorage.getItem('body'));        
			if (this.user.is_wash_man==true ) {
				this._router.navigate(['/dashboard/wash']);
			}
			else if (this.user.is_delivery_man==true){
				this._router.navigate(['/dashboard/delivery']);
			}
		}

	ngOnInit() {
	}

}
