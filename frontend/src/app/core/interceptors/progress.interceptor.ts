import {finalize, tap} from 'rxjs/operators';
import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest,
  HttpResponse
} from '@angular/common/http';
import {Observable} from 'rxjs';
import {ProgressBarService} from '../services/progress-bar.service';
import {error} from "@angular/compiler/src/util";

export class ProgressInterceptor implements HttpInterceptor {
  constructor(
    public progressBarService: ProgressBarService
  ) {
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    this.progressBarService.increase();
    return next
      .handle(req).pipe(
        tap(event => {
          if (event instanceof HttpResponse) {
            this.progressBarService.decrease();
          }
        }),
        finalize(() => {
          this.progressBarService.decrease();
        })
      );
  }
}
