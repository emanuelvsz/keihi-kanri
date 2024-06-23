import { getHealthMessage } from "../services/health";

export const fetchHealthMessage = async () => {
    return await getHealthMessage();
};