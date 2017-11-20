import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardWashComponent } from './dashboard-wash.component';

describe('DashboardWashComponent', () => {
  let component: DashboardWashComponent;
  let fixture: ComponentFixture<DashboardWashComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DashboardWashComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboardWashComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
