import { Component, OnInit } from '@angular/core';
import { Router }       from '@angular/router';
import { AuthService }      from '../app.service';

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {
  	toogle=0
	public isCollapsed:boolean = true;
	constructor(private _router: Router, private _auth: AuthService) { }

	ngOnInit() {
	}
	onClickLogout(e){
		e.preventDefault();
		this._auth.logout();
		this._router.navigate(['/login']);
	}
}
