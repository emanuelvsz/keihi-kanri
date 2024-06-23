import { fetchHealth } from "../../adapters/api/client";
import { HealthModel } from "../models/health";

export const getHealthMessage = async (): Promise<HealthModel> => {
  const data = await fetchHealth();
  return new HealthModel(data as string);
};