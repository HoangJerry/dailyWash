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
    user;
    title = "Ngoc Hoang"
    errors = [];
    isLoginpage = false;
    constructor(private _router: Router, private _api: AppService){
      // console.log(this._router);
      
      this.user=JSON.parse(localStorage.getItem('body'));     
      if (this.user){
        if (this.user.is_wash_man==true || this.user.is_delivery_man==true){
          this._router.navigate(['/dashboard']);
        }
      else{
          // this._router.events.subscribe(
          // (url:any) => {
          //   console.log(url.url);
            // if (url.url=="/app" || url.url=="/") {
              // this._router.navigate(['/home']);
          //   }
          // });
        }
      };
    };
}
