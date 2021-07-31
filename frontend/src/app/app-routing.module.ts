import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {Error404PageComponent} from './shared/pages/error404-page/error404-page.component';
import {AppConfig} from './configs/app.config';
import {HomePageComponent} from './shared/pages/home-page/home-page.component';
import {AuthGuardService} from './core/guards/auth-guard.service';

const routes: Routes = [
  {path: 'home', component: HomePageComponent, pathMatch: 'full'},
  {path: AppConfig.routes.heroes, loadChildren: './modules/heroes/heroes.module#HeroesModule'},

  {path: '', redirectTo: 'home', pathMatch: 'full'},

  // {path: '', redirectTo: AppConfig.routes.account, pathMatch: 'full'},
  // {path: AppConfig.routes.auth, loadChildren: './modules/auth/auth.module#AuthModule'},

  // {
  //   path: '',
  //   canActivate: [AuthGuardService],
  //   children: [
  //     {
  //       path: AppConfig.routes.profile,
  //       loadChildren: './modules/profile/profile.module#ProfileModule'
  //     },
  //   ]
  // },

  {path: AppConfig.routes.error404, component: Error404PageComponent},

  // otherwise redirect to 404
  {path: '**', redirectTo: '/' + AppConfig.routes.error404}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, {
      scrollPositionRestoration: 'enabled',
      anchorScrolling: 'enabled'
    })
  ],
  exports: [
    RouterModule
  ]
})

export class AppRoutingModule {
}
