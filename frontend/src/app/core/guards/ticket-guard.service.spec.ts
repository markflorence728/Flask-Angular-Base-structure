import { TestBed } from '@angular/core/testing';

import { TicketGuardService } from './ticket-guard.service';

describe('TicketGuardService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TicketGuardService = TestBed.get(TicketGuardService);
    expect(service).toBeTruthy();
  });
});
