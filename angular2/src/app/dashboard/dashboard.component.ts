import { Component, OnInit } from '@angular/core';
import { AppService }        from '../app.service';

import { Router } from '@angular/router'

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  errors = [];
  news = [];
  mytakings = [];
  returnings = [];
  myreturnings = [];
  constructor(private route: Router,private _api: AppService) {
  }

  ngOnInit() {
    this.myPending();
  }
  myPending(){
    this._api.OrderNew()
            .subscribe(
              (res:any) => {
                // res.results.map(function(obj,key){
                //   console.log(key);
                // })
                this.news = res.results;
              },
              (error:any) =>  this.errors = error
          );
    this._api.OrderReturning()
            .subscribe(
              (res:any) => {
                this.returnings = res.results;
              },
              (error:any) =>  this.errors = error
          );
    this._api.OrderMeTaking()
            .subscribe(
              (res:any) => {
                this.mytakings = res.results;
              },
              (error:any) =>  this.errors = error
          );
    this._api.OrderMeReturning()
            .subscribe(
              (res:any) => {
                this.myreturnings = res.results;
              },
              (error:any) =>  this.errors = error
          );
  }
  move(id){
    this._api.TakingOrder(id)
              .subscribe(
                        (res:any) => {
                          this.myPending();
                        },
                        (error:any) =>  this.errors = error
              );
  }
}


