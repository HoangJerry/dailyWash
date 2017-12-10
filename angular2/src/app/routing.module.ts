import { Routes, RouterModule }     from '@angular/router';

import { AppComponent }         from './app.component';
import { UserDetailComponent }      from './user-detail/user-detail.component';
import { UserListComponent }        from './user-list/user-list.component';
import { LoginComponent }           from './login/login.component';
import { DashboardComponent }       from './dashboard/dashboard.component';
import { UserOrderComponent } from './user-order/user-order.component';
import { DashboardWashComponent } from './dashboard-wash/dashboard-wash.component';
import { HomeComponent } from './home/home.component';
import { DashboardMainComponent } from './dashboard-main/dashboard-main.component';
import { SignupComponent } from './signup/signup.component';
import { SignupSuccessComponent } from './signup-success/signup-success.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

import { AuthGuard }              from './app.service';

export const routes: Routes = [
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full',
  }, 
  {
    path: 'app',
    component: AppComponent,
    canActivate:[AuthGuard],
  },
  {
    path: 'dashboard',
    component: DashboardMainComponent,
    canActivate:[AuthGuard],
    // children: [
    //   {
    //     path: 'detail/:id',
    //     component: UserDetailComponent
    //   },
    // ]
    children: [
      {
        path: 'wash',
        component: DashboardWashComponent
      },
      {
        path: 'delivery',
        component: DashboardComponent,
      },
    ]
  },
  {
    path: 'login',
    component: LoginComponent,
  },

  {
    path: 'signup',
    component: SignupComponent,
  },
  {
    path: 'success',
    component: SignupSuccessComponent
  },
  {
    path: 'home',
    component: HomeComponent,
    canActivate:[AuthGuard]
  },
  {
    path: 'product/:id',
    component: ProductDetailComponent,
    canActivate:[AuthGuard]
  },
  {
    path: 'order',
    component: UserOrderComponent,
    canActivate:[AuthGuard]
  },

];

