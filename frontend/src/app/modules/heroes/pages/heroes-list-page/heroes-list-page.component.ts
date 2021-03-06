import {Component, Inject, OnInit, PLATFORM_ID, ViewChild} from '@angular/core';
import {Hero} from '../../shared/hero.model';
import {HeroService} from '../../shared/hero.service';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import {MatDialog, MatSnackBar} from '@angular/material';
import {Router} from '@angular/router';
import {AppConfig} from '../../../../configs/app.config';
import {UtilsHelperService} from '../../../../core/services/utils-helper.service';
import {HeroRemoveComponent} from '../../components/hero-remove/hero-remove.component';
import {isPlatformBrowser} from '@angular/common';

@Component({
  selector: 'app-heroes-list-page',
  templateUrl: './heroes-list-page.component.html',
  styleUrls: ['./heroes-list-page.component.scss'],
  animations: [UtilsHelperService.fadeInOut()]
})

export class HeroesListPageComponent implements OnInit {

  heroes: Hero[];
  newHeroForm: FormGroup;
  canVote = false;
  error: boolean;

  @ViewChild('form') myNgForm; // just to call resetForm method

  constructor(private heroService: HeroService,
              private dialog: MatDialog,
              private snackBar: MatSnackBar,
              private router: Router,
              private formBuilder: FormBuilder,
              @Inject(PLATFORM_ID) private platformId: Object) {
    this.canVote = this.heroService.checkIfUserCanVote();

    this.newHeroForm = this.formBuilder.group({
      'name': new FormControl('', [Validators.required, Validators.maxLength(30)]),
      'alterEgo': new FormControl('', [Validators.required, Validators.maxLength(30)])
    });

    this.onChanges();
  }

  ngOnInit() {
    this.heroService.getHeroes().subscribe((heroes: Array<Hero>) => {
      this.heroes = heroes;
    });
  }

  async createNewHero() {
    if (this.newHeroForm.valid) {
      this.heroService.createHero(new Hero(this.newHeroForm.value)).then(() => {
        this.myNgForm.resetForm();
        this.snackBar.open('Hero created', '', {duration: 1000});
      }, () => {
        this.error = true;
      });
    }
  }

  like(hero: Hero) {
    this.canVote = this.heroService.checkIfUserCanVote();
    if (this.canVote) {
      hero.like();
      if (isPlatformBrowser(this.platformId)) {
        localStorage.setItem('votes', '' + (Number(localStorage.getItem('votes')) + 1));
      }
      this.heroService.updateHero(hero);
    } else {
      this.snackBar.open('Can\'t vote anymore', '', {duration: 1000});
    }
  }

  deleteHero(hero: Hero) {
    const dialogRef = this.dialog.open(HeroRemoveComponent);
    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.heroService.deleteHero(hero.id).then(() => {
          this.heroService.showSnackBar('Hero removed');
        }, () => {
          this.error = true;
        });
      }
    });
  }

  seeHeroDetails(hero): void {
    if (hero.default) {
      this.router.navigate([AppConfig.routes.heroes + '/' + hero.id]);
    }
  }

  private onChanges() {
    this.newHeroForm.get('name').valueChanges.subscribe((value) => {
      if (value && value.length >= 3 && UtilsHelperService.isPalindrome(value)) {
        this.snackBar.open('Yeah that\'s a Palindrome!', '', {duration: 2000});
      } else {
        this.snackBar.dismiss();
      }
    });
  }
}
