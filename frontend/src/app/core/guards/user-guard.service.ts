import {Injectable} from '@angular/core';
import {MeService} from "../auth/me.service";
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from "@angular/router";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UserGuardService implements CanActivate{

  failedUrl?: string = null;

  constructor(
    private me: MeService,
    private router: Router
  ) {
  }

  popFailedUrl(): string {
    let url = this.failedUrl;
    this.failedUrl = null;
    return url;
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    if (this.me.user) {
      return Promise.resolve(true);
    }

    this.failedUrl = state.url;
    this.router.navigate(['/auth/login']);
    return Promise.resolve(false);
  }
}
