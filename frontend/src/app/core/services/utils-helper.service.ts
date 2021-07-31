import {Injectable} from '@angular/core';
import {animate, AnimationTriggerMetadata, style, transition, trigger} from '@angular/animations';

declare const require;
const bowser = require('bowser');

@Injectable({
  providedIn: 'root'
})
export class UtilsHelperService {
  static fadeInOut(): AnimationTriggerMetadata {
    return trigger('fadeInOut', [
      transition(':enter', [
        style({opacity: 0}),
        animate(500, style({opacity: 1}))
      ]),
      transition(':leave', [
        animate(500, style({opacity: 0}))
      ])
    ]);
  }

  static isPalindrome(str) {
    const len = Math.floor(str.length / 2);
    for (let i = 0; i < len; i++) {
      if (str[i] !== str[str.length - i - 1]) {
        return false;
      }
    }
    return true;
  }

  static isBrowserValid() {
    const browser = bowser.getParser(window.navigator.userAgent);

    return browser.satisfies({
      windows: {
        'internet explorer': '>10',
      },
      macos: {
        safari: '>10.1'
      },
      mobile: {
        safari: '>=9',
        'android browser': '>3.10'
      },
      chrome: '>20.1.1432',
      chromium: '>20.1.1432',
      firefox: '>31',
      opera: '>22'
    });
  }

  static getCountryCode(internationalNumber: string) {
    return internationalNumber.split(' ')[0]
  }

  static getPhoneNumber(internationalNumber: string) {
    let number = '';
    let arr = internationalNumber.split(' ');

    for(let i=1; i<arr.length; i++) {
      number += arr[i]
    }

    return number;
  }

  static getStringDateFromDateTime(datetime: any) {
    let date = new Date(datetime);
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let day = date.getDate();

    return month + '/' + day + '/' + year;
  }
}
