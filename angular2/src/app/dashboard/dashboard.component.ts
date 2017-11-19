import { Component, OnInit, TemplateRef }  from '@angular/core';
import { AppService,ChatService }         from '../app.service';
import { BsModalService }     from 'ngx-bootstrap/modal';
import { BsModalRef } from 'ngx-bootstrap/modal/bs-modal-ref.service';
import { Router, ActivatedRoute } from '@angular/router'

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
  washMans = [];
  private fragment: string;
  modalRef: BsModalRef;
  selectedValue:any;

  onChangeWashMan(newObj) {
    console.log(newObj);
    this.selectedValue = newObj;
    console.log(this.selectedValue.first_name)
    // ... do other stuff here ...
  }
  constructor(
    private route: Router,
    private _api: AppService,
    private _chat: ChatService,
    private activeRoute: ActivatedRoute,
    private modalService: BsModalService,) {
  }
  openModal(template: TemplateRef<any>) {
    this.modalRef = this.modalService.show(template);
  }

  ngOnInit() {
    this.myPending();
    this.activeRoute.fragment.subscribe(fragment => { 
      this.fragment = fragment; 
          try {
      document.querySelector('#' + this.fragment).scrollIntoView();
    } catch (e) { console.log(e)}

    });

  }

  ngAfterViewInit(): void {
    try {
      document.querySelector('#' + this.fragment).scrollIntoView();
    } catch (e) { console.log(e)}
  }

  myPending(){
    this._api.WashManList()
          .subscribe(
              (res:any) => {
                this.washMans = res.results;
                console.log(this.washMans);
              },
              (error:any) =>  this.errors = error
          );
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

  moveReturn(id){
    this._api.ReturningOrder(id)
              .subscribe(
                        (res:any) => {
                          this.myPending();
                        },
                        (error:any) =>  this.errors = error
              );
  }
}


