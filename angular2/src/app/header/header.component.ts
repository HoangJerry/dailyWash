import { Component, OnInit,ViewEncapsulation } from '@angular/core';
import { Router }       from '@angular/router';
import { AuthService }      from '../app.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class HeaderComponent implements OnInit {
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
