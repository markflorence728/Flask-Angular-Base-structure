import {Injectable} from '@angular/core';
import {ApiRequestService} from './api-request.service';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private request: ApiRequestService) {
  }

  auth = {
    facebook_login: (facebook_user: any) => this.request
      .post(facebook_user)
      .url('/api/v1.0/auth/facebook_login')
      .comment('Facebook Login Request'),
    email_login: (email_login: any) => this.request
      .post(email_login)
      .url('/api/v1.0/auth/email_login')
      .comment('Email Login Request'),
    email_check: (email) => this.request
      .post(email)
      .url('/api/v1.0/auth/email_check')
      .comment('Email Check Request'),
    register_phone: (register_phone: any) => this.request
      .post(register_phone)
      .url('/api/v1.0/auth/register_phone')
      .comment('Register Phone Request'),
    complete_profile: (id, complete_info) => this.request
      .put()
      .url('/api/v1.0/auth/complete_profile/{}', id)
      .payload(complete_info)
      .comment('Complete Profile Request'),
    logout: () => this.request
      .delete()
      .url('/api/v1.0/auth/logout')
      .auth()
      .comment("Logout Request")
  };

  me = {
    get: () => this.request
      .get()
      .url('/api/v1.0/me')
      .auth()
      .comment("Get my info"),
  };

  users = {
    update: (id, user) => this.request
      .put()
      .url('api/v1.0/users/{}', id)
      .payload(user)
      .auth()
      .comment("Update User Info"),
  };

  tickets = {
    list: (user_id) => this.request
      .get()
      .url('/api/v1.0/tickets/user_tickets/{}', user_id)
      .auth()
      .comment("Get user tickets"),
    get: (ticket_number) => this.request
      .get()
      .url('/api/v1.0/tickets/{}', ticket_number)
      .auth()
      .comment("Get ticket info"),
    match: (ticket_number) => this.request
      .get()
      .url('/api/v1.0/tickets/match/{}', ticket_number)
      .auth()
      .comment("Match(Validate) ticket and user"),
  };

  transfers = {
    get: (event_id) => this.request
      .get()
      .url('/api/v1.0/transfers/active/{}', event_id)
      .auth()
      .comment("Get user's active transfer"),
  }
}
