import { Component, OnInit } from '@angular/core';
import { AppService }        from '../app.service';
import { AuthService } 	     from '../app.service';
import { Router }	         from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user;
  email:string = '';
  password:string = '';
  phone:string = '';
  isRegister:boolean = false;
  errors = [];
  constructor(private _router: Router, private _api: AppService, private _auth: AuthService){
    
  };

  ngOnInit() {
  }
  onClickLogin(){
  	this._api.UserLogin(this.email,this.password)
	        .subscribe(
	            (res:any) => {
                let payload = res.json();
                localStorage.setItem('body',res._body);
                this._auth.login(payload.token);    
                this.user=JSON.parse(localStorage.getItem('body'));        
                if (this.user.is_wash_man==true || this.user.is_delivery_man==true){
                  this._router.navigate(['/dashboard']);
                }
                else {
                  this._router.navigate(['/home']);
                }
	            },
	            (error:any) =>  this.errors = error
	        );
  }
}
