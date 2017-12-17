import { Component, OnInit, HostListener } 	from '@angular/core';
import { AppService }					from '../app.service';
@Component({
  selector: 'app-user-history',
  templateUrl: './user-history.component.html',
  styleUrls: ['./user-history.component.css']
})
export class UserHistoryComponent implements OnInit {
  histories=[];
  next;
  constructor(
  	private _api: AppService,
  ) 
	  {
	  	this._api.OrderList(-1,1,0,0,0)
	  			.subscribe(
	  				(res)=>{
	  					this.histories=res.results;
	  					this.next=res.next;
	  				}
	  			)
	  }

  ngOnInit() {
  	// window.addEventListener('scroll', this.scroll, true);
  }

	@HostListener('window:scroll', ['$event']) onScrollEvent($event){
	  console.log($event);
	  console.log("scrolling");
	} 
}
