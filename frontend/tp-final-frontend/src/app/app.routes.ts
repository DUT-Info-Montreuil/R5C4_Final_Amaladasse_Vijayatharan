import { Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { AccueilComponent } from './accueil/accueil.component';
import { ListeComponent } from './liste/liste.component';
import { GraphiquesComponent } from './graphiques/graphiques.component';

export const routes: Routes = [
    { path: '', component: AccueilComponent },
    { path: 'liste', component: ListeComponent },
    { path: 'graphiques', component: GraphiquesComponent },
];
