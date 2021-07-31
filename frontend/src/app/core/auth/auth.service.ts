import {Injectable} from '@angular/core';
import {ApiService} from '../http/api.service';
import {MeService} from './me.service';
import {Router} from "@angular/router";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private api: ApiService,
    private router: Router,
    private me: MeService
  ) {
  }

  static rememberToken(token) {
    localStorage.setItem('8ddsql.token', token);
  }

  static getToken() {
    return localStorage.getItem('8ddsql.token');
  }

  static canAutoLogin(): boolean {
    return AuthService.getToken() !== null;
  }

  isAuthenticated(): boolean {
    return this.me.token !== null;
  }

  autoLogin(): Promise<any> {
    const token = AuthService.getToken();
    if (token === null) {
      return Promise.reject({'error': 'No saved user session'});
    }
    this.me.setToken(token);
    return this.api.me.get().promise()
      .then(user => {
        this.me.setUser(user);
      });
  }

  logout(): Promise<any> {
    this.api.auth.logout().promise();
    this.me.forget();
    localStorage.removeItem('8ddsql.token');
    this.router.navigate(['/auth/login']);
    return ;
  }
}

