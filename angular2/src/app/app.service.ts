import { Http, Headers, Response, RequestOptions }  from "@angular/http"
import { Injectable,Inject }        from '@angular/core';
import { Router }                   from '@angular/router';
import { IUser }                    from './app'
import { CanActivate }              from '@angular/router';
import { Observable }               from 'rxjs/Observable';
import { Observer }                 from 'rxjs/Observer';
import 'rxjs/Rx';
import 'rxjs/add/operator/map';

import { WebSocketBridge } from 'django-channels'

@Injectable()
export class ChatService {
    
    constructor() { 
        const webSocketBridge = new WebSocketBridge();
        webSocketBridge.connect('ws://localhost:8000/');

        webSocketBridge.socket.onmessage = function (e) {
                        console.log("Return value");
          let obj = JSON.parse(e.data);
          console.log(obj.payload.data);
        };
        webSocketBridge.socket.onopen = function () {
            let data = {
                stream: "orders",
                payload: {
                  action: "subscribe",
                  data: {
                    action:"update"
                  },
                }
            }
            let mgs = JSON.stringify(data)
            webSocketBridge.socket.send(mgs)
        };    
        webSocketBridge.socket.onclose = function () {
                console.log("Disconnected from socket");
        };
    }
}

@Injectable()
export class AppService {
    private _router: Router; 
    private _auth:AuthService;
    // API url:
    // private apiUrl = 'http://dailywash.pythonanywhere.com/api';
    private apiUrl = 'http://localhost:8000/api';

	private headers = new Headers({'Content-Type': 'application/json'});

  	constructor(@Inject(Http) private _http: Http)
    {
        // this.headers.append('Content-Type', 'application/x-www-form-urlencoded');
        // this.headers.append('X-Requested-With', 'XMLHttpRequest');
        // this.headers.append('token', 'abc'); 
        
    // API url:
    }

    public UserList(){
        let url = this.apiUrl+'/user/all/';
        // return this._http.get(url, {headers: this.headers})
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }
    public UserMe(){
        let url = this.apiUrl+'/user/me/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public WashManList(){
        let url = this.apiUrl+'/user/washman/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public CitiesList(){
        let url = this.apiUrl+'/address/city/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public DistrictsList(id){
        let url = this.apiUrl+'/address/city/'+id+'/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public CategoriesList(){
        let url = this.apiUrl+'/category/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public ProductList(category_id="",id=""){
        let url = this.apiUrl+'/product/?';
        if (category_id){
            url += 'category_id='+category_id;
        }
        if (id){
            url += 'id='+id;
        }
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

    public UserSignUp(firstname,lastname,city,district,address,email,phone){
        let url = this.apiUrl+'/user/signup/';
        let data={
            email:email,
            first_name:firstname,
            last_name:lastname,
            phone:phone,
            city:city,
            district:district,
            street:address,
        }
        return this._http.post(url,data,{headers: this.headers})
                        // .map((res:Response) => res.json())
                        .catch (this.handleError);
    }    

    public UserDetail(id){
        let url = this.apiUrl+'/user/'+id+'/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public UserDelete(id){
        let url = this.apiUrl+'/user/'+id+'/';
        return this._http.delete(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }


    public OrderList(status=-1,user=0,wash_man=0,take_man=0,return_man=0){
        let url = this.apiUrl + '/order/list/?';
        if (status>-1){
            url += '&status='+status;
        }
        if (user){
            url += '&user=1';
        }
        if (wash_man){
            url += '&wash_man=1';
        }
        if (take_man){
            url += '&take_man=1';
        }
        if (return_man){
            url += '&return_man=1';
        }
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token'));
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public OrderDetail(id){
        let url = this.apiUrl+'/order/'+id+'/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
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

    public OrderNew(){
        let url = this.apiUrl + '/order/new/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public OrderReturning(){
        let url = this.apiUrl + '/order/washed/';
        return this._http.get(url)
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public TakingOrder(id){
        let url = this.apiUrl+'/order/taking/';
        let data={
            order_id:id
        }
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.post(url,data,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public ReturningOrder(id){
        let url = this.apiUrl+'/order/returning/';
        let data={
            order_id:id
        }
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.post(url,data,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }
    
    public WashingOrder(id){
        let url = this.apiUrl+'/order/washing/';
        let data={
            order_id:id
        }
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.post(url,data,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

    public OrderMeTaking(){
        let url = this.apiUrl + '/order/me/taking/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }
    public OrderAllTaking(){
        let url = this.apiUrl + '/order/all/taking/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }
    public OrderMeReturning(){
        let url = this.apiUrl + '/order/me/returning/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }
    public OrderMeWashing(){
        let url = this.apiUrl + '/order/me/washing/';
        let head = new Headers({'Content-Type': 'application/json'});
        head.set('Authorization','Token '+localStorage.getItem('token')); 
        return this._http.get(url,{headers: head})
                        .map((res:Response) => res.json())
                        .catch (this.handleError);
    }

	private handleError(error: any): Promise<any> {
        this._auth.logout();
        this._router.navigate(['/login']);
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