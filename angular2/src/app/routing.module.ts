import { Routes, RouterModule }     from '@angular/router';

import { UserDetailComponent }      from './user-detail/user-detail.component';
import { UserListComponent }        from './user-list/user-list.component';
import { LoginComponent }           from './login/login.component';
import { DashboardComponent }       from './dashboard/dashboard.component';
import { UserOrderComponent } from './user-order/user-order.component';

import { AuthGuard }              from './app.service';

export const routes: Routes = [
  {
    path: '',
    redirectTo: '/dashboard',
    pathMatch: 'full',
  },
  {
    path: 'dashboard',
    component: DashboardComponent,
    canActivate:[AuthGuard],
    children: [
      {
        path: 'detail/:id',
        component: UserDetailComponent
      },
    ]
  },
  {
    path: 'login',
    component: LoginComponent,
  },
  {
    path: 'order',
    component: UserOrderComponent,
    canActivate:[AuthGuard]
  }

];

