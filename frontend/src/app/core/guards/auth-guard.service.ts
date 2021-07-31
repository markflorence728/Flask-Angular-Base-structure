import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from '@angular/router';
import {Observable} from 'rxjs';
import {AuthService} from "../auth/auth.service";

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  failedUrl?: string = null;

  constructor(
    private auth: AuthService,
    private router: Router
  ) {
  }

  popFailedUrl(): string {
    let url = this.failedUrl;
    this.failedUrl = null;
    return url;
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    if (this.auth.isAuthenticated()) {
      return Promise.resolve(true);
    } else if (AuthService.canAutoLogin()) {
      return this.auth.autoLogin()
        .then(() => true)
        .catch(() => {
          this.auth.logout();
          this.failedUrl = state.url;
          this.router.navigate(['/auth/login']);
          return false;
        });
    }

    this.failedUrl = state.url;
    this.router.navigate(['/auth/login']);
    return Promise.resolve(false);
  }
}
