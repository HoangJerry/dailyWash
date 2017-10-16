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
                this._router.navigate(['/dashboard']);
	            },
	            (error:any) =>  this.errors = <any>error
	        );
  }
  onClickRegister(e){
    e.preventDefault();
    this.isRegister = !this.isRegister;
    
    // if (this.isRegister)
    //    this.isRegister = false;
    // else
    //   this.isRegister = true;
  }
}
