import {Component, Inject, OnInit, PLATFORM_ID, Renderer2} from '@angular/core';
import {Meta, Title} from '@angular/platform-browser';
import {NavigationEnd, Router} from '@angular/router';
import {MatSnackBar} from '@angular/material';
import {AppConfig} from './configs/app.config';
import {UtilsHelperService} from './core/services/utils-helper.service';
import {DOCUMENT, isPlatformBrowser} from '@angular/common';
import {TranslateService} from '@ngx-translate/core';
import { isString } from 'lodash';

declare const Modernizr;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})

export class AppComponent implements OnInit {

  isOnline: boolean;

  constructor(private title: Title,
              private meta: Meta,
              private snackBar: MatSnackBar,
              private router: Router,
              private translate: TranslateService,
              @Inject(DOCUMENT) doc: Document, renderer: Renderer2,
              @Inject(PLATFORM_ID) private platformId: Object) {
    if (isPlatformBrowser(this.platformId)) {
      this.isOnline = navigator.onLine;
    } else {
      this.isOnline = true;
    }

    translate.setDefaultLang('es');
  }

  ngOnInit() {
    this.title.setTitle('8DD SQL');

    this.onEvents();
    this.checkBrowser();
  }

  onEvents() {
    this.router.events.subscribe((event: any) => {
      if (event instanceof NavigationEnd) {
        switch (event.urlAfterRedirects) {
          case '/':
            this.meta.updateTag({
              name: 'description',
              content: 'Home meta description'
            });
            break;
          case '/' + AppConfig.routes.heroes:
            this.title.setTitle('Heroes list');
            this.meta.updateTag({
              name: 'description',
              content: 'Heroes meta description'
            });
            break;
        }
      }
    });
  }

  checkBrowser() {
    if (isPlatformBrowser(this.platformId)) {
      if (UtilsHelperService.isBrowserValid()) {
        this.checkBrowserFeatures();
      } else {
        this.snackBar.open('Change your browser', 'OK');
      }
    }
  }

  checkBrowserFeatures() {
    let supported = true;
    for (const feature in Modernizr) {
      if (Modernizr.hasOwnProperty(feature) &&
        typeof Modernizr[feature] === 'boolean' && Modernizr[feature] === false) {
        supported = false;
        break;
      }
    }

    if (!supported) {
      this.snackBar.open('Update your browser', 'OK');
    }

    return supported;
  }
}
