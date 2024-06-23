export class HealthModel {
  #message: string;

  constructor(message: string) {
    this.#message = message;
  }

  get message(): string {
    return this.#message
  }
}