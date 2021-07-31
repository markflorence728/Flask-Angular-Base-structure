import {Injectable} from '@angular/core';
import {MatSnackBar, MatSnackBarConfig} from "@angular/material";
import {AppConfig} from "../../configs/app.config";

@Injectable({
  providedIn: 'root'
})
export class SnackBarService {

  config: any;

  constructor(public snackBar: MatSnackBar) {
  }

  public showSnackBar(name): void {
    this.config = new MatSnackBarConfig();
    this.config.duration = AppConfig.snackBarDuration;
    this.snackBar.open(name, 'OK', this.config);
  }
}
