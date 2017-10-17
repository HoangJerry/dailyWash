import { Http, Headers, Response, RequestOptions }  from "@angular/http"
import { Injectable,Inject }        from '@angular/core';
import { Router }                   from '@angular/router';
import { IUser }                    from './app'
import { CanActivate }              from '@angular/router';
import { Observable }               from 'rxjs/Observable';
import { Observer }                 from 'rxjs/Observer';
import 'rxjs/Rx';
import 'rxjs/add/operator/map';

@Injectable()
export class AppService {

	// API url:
    private apiUrl = 'http://dailywash.pythonanywhere.com/api';

	private headers = new Headers({'Content-Type': 'application/json'});

  	constructor(@Inject(Http) private _http: Http)
    {
        // this.headers.append('Content-Type', 'application/x-www-form-urlencoded');
        // this.headers.append('X-Requested-With', 'XMLHttpRequest');
        // this.headers.append('token', 'abc'); 
    }

    public UserList(){
        let url = this.apiUrl+'/user/all/';
        // return this._http.get(url, {headers: this.headers})
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }
    
    public UserLogin(email,password){
        let url = this.apiUrl+'/user/login/';
        let data={
            email:email,
            password:password
        }
        return this._http.post(url,data,{headers: this.headers})
                        // .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public UserDetail(id){
        let url = this.apiUrl+'/user/'+id+'/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

	public UserDelete(id){
        let url = this.apiUrl+'/user/'+id+'/';
		return this._http.delete(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
	}

    public CityData(){
        let url = this.apiUrl + '/address/city/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public DistrictData(id){
        let url = this.apiUrl + '/address/city/'+id+'/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

	private handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }

}

@Injectable()
export class AuthService{
  isLoginSubject :boolean = false;
  isLoggedIn() : boolean {
    this.hasToken();
    return this.isLoginSubject;
  }

  login(token) : void {
    localStorage.setItem('token',token);
    this.isLoginSubject = true; 
    
  }

  logout() : void {
    localStorage.removeItem('token');
    this.isLoginSubject = false;
    localStorage.removeItem('body');
  }

  private hasToken() : void {
    
    if (!localStorage.getItem('token')){
        this.isLoginSubject = false;
    }
    else this.isLoginSubject= true;
  }
}

@Injectable()
export class AuthGuard implements CanActivate {
    constructor(private router: Router, private _auth:AuthService) { }

    canActivate() {
         // not logged in so redirect to login page with the return url
        if (!this._auth.isLoggedIn()) {
            this.router.navigate(['/login']);
            return false;
        }
        return true;
    }
}