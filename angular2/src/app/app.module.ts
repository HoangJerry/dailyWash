import { BrowserModule }    from '@angular/platform-browser';
import { NgModule }         from '@angular/core';
import { RouterModule }     from '@angular/router';
import { HttpModule }       from '@angular/http';
import { FormsModule }      from '@angular/forms';


// Enable Product Mode
import {enableProdMode} from '@angular/core';

import { routes }           from './routing.module';
import { AppService }           from './app.service';
import { AuthService }           from './app.service';
import { AuthGuard }           from './app.service';
import { ChatService }           from './app.service';

// Component
import { AppComponent }         from './app.component';
import { UserDetailComponent }  from './user-detail/user-detail.component';
import { UserListComponent }    from './user-list/user-list.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UserOrderComponent } from './user-order/user-order.component';

// Bootstraps
import { BsDropdownModule } from 'ngx-bootstrap';
import { AlertModule } from 'ngx-bootstrap';
import { CollapseModule } from 'ngx-bootstrap';
import { SideBarComponent } from './side-bar/side-bar.component';
import { LoginComponent } from './login/login.component';
import { ModalModule } from 'ngx-bootstrap';

import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatSelectModule} from '@angular/material';
import {MatInputModule} from '@angular/material';
import {MatButtonModule} from '@angular/material';
import {MatDatepickerModule} from '@angular/material';

import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
const config: SocketIoConfig = { url: 'ws://localhost:8000/', options: {} };
// const config: SocketIoConfig = { url: 'wss://streamer.cryptocompare.com/', options: {} };
@NgModule({
  declarations: [
    AppComponent,
    UserDetailComponent,
    UserListComponent,
    SideBarComponent,
    LoginComponent,
    DashboardComponent,
    UserOrderComponent,
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    RouterModule.forRoot(routes, {
    // useHash: true
    }),
    AlertModule.forRoot(),
    BsDropdownModule.forRoot(),
    CollapseModule.forRoot(),
    BrowserAnimationsModule,
    MatSelectModule,
    MatInputModule,
    MatButtonModule,
    MatDatepickerModule,
    ModalModule.forRoot(),
    SocketIoModule.forRoot(config),
  ],
  providers: [
    AppService,
    AuthService,
    AuthGuard,
    ChatService,
  ],
  // enableProdMode, 
  bootstrap: [AppComponent]
})
export class AppModule { }
