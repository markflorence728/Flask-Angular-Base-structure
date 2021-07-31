export class User {
  id: number;
  facebook_id: string;
  first_name: string;
  last_name: string;
  email: string;
  email_verified: boolean;
  phone: string;
  phone_verified: boolean;
  gender: string;
  birthday: string;
  zipcode: string;
  city: string;
  photo_url: string;
  complete_profile: boolean;
}

export class Event {
  id: number;
  cashless_id: number;
  name: string;
  max_balance: number;
  max_promo: number;
  photo_url: string;
}

export class Ticket {
  id: number;
  ticket: string;
  event_id: number;
  user_id: number;
  is_active: boolean;
  event: Event;
  user: User;
}

export class Transaction {
  id: number;
  event_id: number;
  user_id: number;
  amount: number;
  currency: string;
  pay_mode: string;
}

export class Transfer {
  id: number;
  uid: string;
  event_id: number;
  user_id: number;
  balance: number;
  promo_balance: number;
  dev_mac: string;
  nfc_id: string;
  status: string;
}

export class Product {
  id: number;
  name: string;
  amount: number;
  promo_amount: number;
  is_active: boolean;
}
