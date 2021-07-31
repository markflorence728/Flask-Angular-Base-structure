import {Injectable} from '@angular/core';
import {Ticket, User} from "../../shared/models/models";

@Injectable({
  providedIn: 'root'
})
export class MeService {
  token?: string = null;
  user?: User = null;
  ticket_number?: string = null;
  ticket?: Ticket = null;

  constructor() {
  }

  setToken(token: string) {
    this.token = token;
  }

  setUser(user: any) {
    this.user = user;
  }

  static rememberTicketNumber(ticket_number) {
    localStorage.setItem('8ddsql.ticket_number', ticket_number);
  }

  static getTicketNumber() {
    return localStorage.getItem('8ddsql.ticket_number');
  }

  static removeTicketNumber() {
    localStorage.removeItem('8ddsql.ticket_number');
  }

  setTicket(ticket: any) {
    this.ticket = ticket
  }

  forget() {
    this.user = null;
    this.token = null;
    this.ticket = null;
    MeService.removeTicketNumber()
  }

  // hasRole(role: string): boolean {
  //   if (this.user === null) {
  //     return false;
  //   }
  //   return some(this.user.roles, roleName => roleName === role);
  // }
}
