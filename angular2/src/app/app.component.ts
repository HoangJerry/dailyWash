import { Component }    from '@angular/core';
import { Router}       from '@angular/router';

import { AppService }   from './app.service';
// declare var $:any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
    title = "Ngoc Hoang"
    errors = [];
    isLoginpage = false;
    constructor(private _router: Router, private _api: AppService){
      this._router.events.subscribe(
        (url:any) => {
          this.isLoginpage=false;
          if (url.url=="/login") {this.isLoginpage=true}
        }
      );
    };
}
