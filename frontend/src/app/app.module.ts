import {ErrorHandler, NgModule} from '@angular/core';
import {AppRoutingModule} from './app-routing.module';
import {CoreModule} from './core/core.module';
import {AppComponent} from './app.component';
import {APP_CONFIG, AppConfig} from './configs/app.config';
import {SharedModule} from './shared/shared.module';
import {NgxExampleLibraryModule} from '@ismaestro/ngx-example-library';
import {FirebaseModule} from './shared/modules/firebase.module';
import {SentryErrorHandler} from './core/sentry.errorhandler';
import {BrowserModule} from '@angular/platform-browser';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {registerLocaleData} from '@angular/common';
import localeEs from '@angular/common/locales/es';
import localeFrEs from '@angular/common/locales/extra/es';

import {TranslateLoader, TranslateModule} from '@ngx-translate/core';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';

registerLocaleData(localeEs, localeFrEs);

@NgModule({
  imports: [
    BrowserModule.withServerTransition({appId: '8ddsql'}),
    HttpClientModule,
    FirebaseModule,
    NgxExampleLibraryModule.forRoot({
      config: {
        say: 'hello'
      }
    }),
    CoreModule,
    SharedModule,
    AppRoutingModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpClient]
      }
    })
  ],
  declarations: [
    AppComponent,
  ],
  providers: [
    {provide: APP_CONFIG, useValue: AppConfig},
    {provide: ErrorHandler, useClass: SentryErrorHandler},
  ],
  bootstrap: [AppComponent]
})

export class AppModule {
}

export function HttpLoaderFactory(http: HttpClient) {
    return new TranslateHttpLoader(http);
}
