import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from "@angular/router";
import {Observable} from "rxjs";
import {MeService} from "../auth/me.service";
import {ApiService} from "../http/api.service";

@Injectable({
  providedIn: 'root'
})
export class TicketGuardService implements CanActivate {

  failedUrl?: string = null;

  constructor(
    private me: MeService,
    private router: Router,
    private api: ApiService,
  ) {
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    if (this.me.ticket) {
      return Promise.resolve(true);
    } else if (MeService.getTicketNumber()) {
      return this.api.tickets.get(MeService.getTicketNumber()).promise()
        .then(resp => {
          console.log(resp);

          this.me.setTicket(resp);
          return true;
        })
        .catch(e => {
          console.log(e);

          MeService.removeTicketNumber();
          return false;
        })
    }

    this.failedUrl = state.url;
    this.router.navigate(['/account/connect-ticket']);
    return Promise.resolve(false);
  }
}
