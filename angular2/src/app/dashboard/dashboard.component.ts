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
  constructor(private route: Router,private _api: AppService) {
  }

  ngOnInit() {
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
  }

  move(id){
    this._api.TakingOrder(id)
              .subscribe(
                        (res:any) => {
                          res.results.map(function(obj,key){
                            console.log(obj);
                          })
                          // this.news = res.results;
                        },
                        (error:any) =>  this.errors = error
              );
  }
}


