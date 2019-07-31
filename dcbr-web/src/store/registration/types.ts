export interface ProfileTypes {
  firstName: string;
  middleName: string;
  lastName: string;
  commType: string;
  phone: string;
  email: string;
  streetNumber: number;
  aptNumber: number;
  streetName: string;
  city: string;
  postalCode: string;
  homeAsOperation: boolean;
}

export interface RegistrationState {
  profile?: ProfileTypes;
  error: boolean;
}
