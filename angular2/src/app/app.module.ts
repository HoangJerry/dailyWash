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
import { DashboardWashComponent } from './dashboard-wash/dashboard-wash.component';
import { DashboardMainComponent } from './dashboard-main/dashboard-main.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { SignupComponent } from './signup/signup.component';
import { SignupSuccessComponent } from './signup-success/signup-success.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';


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
import {MatTabsModule} from '@angular/material/tabs';

import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { HomeComponent } from './home/home.component';
import { UserHistoryComponent } from './user-history/user-history.component';
const config: SocketIoConfig = { url: 'ws://localhost:9000/', options: {'transports': ['websocket', 'flashsocket', 'htmlfile', 'xhr-polling', 'jsonp-polling']} };
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
    DashboardWashComponent,
    HomeComponent,
    DashboardMainComponent,
    HeaderComponent,
    FooterComponent,
    SignupComponent,
    SignupSuccessComponent,
    ProductDetailComponent,
    UserHistoryComponent,
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
    MatTabsModule,
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
