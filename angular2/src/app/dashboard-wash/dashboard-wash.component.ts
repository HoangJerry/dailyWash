import { Component, OnInit,TemplateRef } from '@angular/core';
import { AppService, ChatService }         from '../app.service';
import { BsModalService }     from 'ngx-bootstrap/modal';
import { BsModalRef } from 'ngx-bootstrap/modal/bs-modal-ref.service';
import { Router, ActivatedRoute } from '@angular/router'

@Component({
  selector: 'app-dashboard-wash',
  templateUrl: './dashboard-wash.component.html',
  styleUrls: ['./dashboard-wash.component.css']
})
export class DashboardWashComponent implements OnInit {
  errors = [];
  news = [];
  mywashings = [];
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
    private activeRoute: ActivatedRoute,
    private modalService: BsModalService,
) {
    
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
    this._api.OrderAllTaking()
            .subscribe(
              (res:any) => {
                // res.results.map(function(obj,key){
                //   console.log(key);
                // })
                this.news = res.results;
              },
              (error:any) =>  this.errors = error
          );
    this._api.OrderMeWashing()
            .subscribe(
              (res:any) => {
                this.mywashings = res.results;
              },
              (error:any) =>  this.errors = error
          );
  }

  orderDetail(id){
    this._api.OrderDetail(id)
      .subscribe(
          (res:any) => {
            this.selectedValue = res.results;
          },
          (error:any) =>  this.errors = error
      );
  }
  
  moveWash(id){
    this._api.WashingOrder(id)
              .subscribe(
                        (res:any) => {
                          this.myPending();
                        },
                        (error:any) =>  this.errors = error
              );
  }
  
}
